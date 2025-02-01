import React from "react";

export async function getStaticProps() {
  const res = await fetch("http://localhost:3100/projects");

  // API 호출 실패 시 404 페이지 반환
  if (!res.ok) {
    return {
      notFound: true,
    };
  }

  const projects = await res.json();

  return {
    props: { projects },
    revalidate: 10 
  };
}

interface Project {
  name: string;
  // 다른 필요한 팀 속성들도 여기에 추가하세요
}

function ProjectsPage({ projects }: { projects: Project[] }) {
  return (
    <div>
      <h1>프로젝트정보</h1>
      {projects.map((project: Project) => (
        <p key={project.name}>{project.name}</p>
      ))}
    </div>
  );
}

export default ProjectsPage;