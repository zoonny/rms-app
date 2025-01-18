import useSWR from 'swr';

const ROOT_URL = 'https://jsonplaceholder.typicode.com';

export default function usePost(id) {
  const fetcher = (...args) => fetch(...args).then((response) => response.json());
  const { data, error, isLoading } = useSWR(`${ROOT_URL}/posts/${id}`, fetcher);

  return {
    post: data,
    error: error,
    isLoading
  };
}
