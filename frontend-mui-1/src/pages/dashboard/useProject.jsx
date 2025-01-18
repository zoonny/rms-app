import useSWR from 'swr';

const ROOT_URL = 'http://localhost:8000/api';
// const ROOT_URL = 'http://172.17.0.1:8000/api';

export default function useProject(skip, limit) {
  const fetcher = (...args) => fetch(...args).then((response) => response.json());
  const { data, error, isLoading } = useSWR(`${ROOT_URL}/projects?skip=${skip}&limit=${limit}`, fetcher);

  return {
    data: data,
    error: error,
    isLoading
  };
}
