import React from "react";

export async function getServerSideProps(context) {
  const res = await fetch("http://localhost:3100/teams");

  // API 호출 실패 시 404 페이지 반환
  if (!res.ok) {
    return {
      notFound: true,
    };
  }

  const teams = await res.json();

  return {
    props: { teams },
  };
}

interface Team {
  name: string;
  // 다른 필요한 팀 속성들도 여기에 추가하세요
}

function TeamsPage({ teams }: { teams: Team[] }) {
  return (
    <div>
      <h1>조직정보</h1>
      {teams.map((team, index) => (
        <p key={index}>{team.name}</p>
      ))}
    </div>
  );
}

export default TeamsPage;
