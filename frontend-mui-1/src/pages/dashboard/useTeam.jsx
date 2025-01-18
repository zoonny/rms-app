import useSWR from 'swr';

const ROOT_URL = 'http://localhost:8000/api';

export default function useTeam(skip, limit) {
  const fetcher = (...args) => fetch(...args).then((response) => response.json());
  const { data, error, isLoading } = useSWR(`${ROOT_URL}/teams?skip=${skip}&limit=${limit}`, fetcher);

  return {
    data: data,
    error: error,
    isLoading
  };
}
