import { useState, useEffect, Suspense } from "react";
import { LucideIcon } from "lucide-react";

export default function DynamicLucideIcon({ iconName, className = "size-4 shrink-0" }: { iconName: string, className?: string }) {
  const [IconComponent, setIconComponent] = useState<LucideIcon | null>(null);

  useEffect(() => {
    async function loadIcon() {
      try {
        const { [iconName]: LucideIcon } = await import("lucide-react");
        setIconComponent(() => LucideIcon);
      } catch (error) {
        console.error(`Error loading icon: ${iconName}`, error);
      }
    }

    loadIcon();
  }, [iconName]);

  if (!IconComponent) return undefined;

  return <div>{IconComponent && <IconComponent className={className} />}</div>;
}
