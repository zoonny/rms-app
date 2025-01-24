import { AlertCircle } from "lucide-react";

import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert";

export function AlertMessage({
  title = "Error",
  description = "Please try again later.",
}: {
  title?: string;
  description?: string;
}) {
  return (
    <Alert variant="destructive" className="h-12 pt-1.5">
      <AlertCircle className="h-4 w-4" />
      <AlertTitle>{title}</AlertTitle>
      <AlertDescription className="text-xs">{description}</AlertDescription>
    </Alert>
  );
}
