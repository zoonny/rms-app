"use client"

import * as React from "react"
import {
  AudioWaveform,
  BookOpen,
  Bot,
  Command,
  Frame,
  GalleryVerticalEnd,
  Map,
  PieChart,
  Settings2,
  SquareTerminal,
} from "lucide-react"

import { NavMain } from "@/components/layout/nav-main"
import { NavProjects } from "@/components/layout/nav-projects"
import { NavUser } from "@/components/layout/nav-user"
import { TeamSwitcher } from "@/components/layout/team-switcher"
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
  SidebarRail,
} from "@/components/ui/sidebar"
import useTeam from "@/hooks/use-team"
import { Skeleton } from "../ui/skeleton"
import useUser from "@/hooks/use-user"
import useProject from "@/hooks/use-project"

export function AppSidebar({ ...props }: React.ComponentProps<typeof Sidebar>) {
  const { data: teams, error: teamsError, isLoading: teamsIsLoading } = useTeam("teams")
  const { data: user, error: userError, isLoading: userIsLoading } = useUser("user")
  const { data: menus, error: menusError, isLoading: menusIsLoading } = useUser("menus")
  const { data: projects, error: projectsError, isLoading: projectsIsLoading } = useProject("projects")

  return (
    <Sidebar collapsible="icon" {...props}>
      <SidebarHeader>
        {teamsIsLoading? <Skeleton className="h-12 w-full" /> : <TeamSwitcher teams={teams}/>}
      </SidebarHeader>
      <SidebarContent>
        {menusIsLoading ? undefined : <NavMain title="팀" items={menus} />}
        {projectsIsLoading ? undefined : <NavProjects title="프로젝트" projects={projects} />}
      </SidebarContent>
      <SidebarFooter>
        {userIsLoading ? <Skeleton className="h-12 w-full" /> : <NavUser user={user} />}
      </SidebarFooter>
      <SidebarRail />
    </Sidebar>
  )
}
