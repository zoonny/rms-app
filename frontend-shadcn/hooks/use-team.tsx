import useSWR from "swr";
import api from "@/lib/api";

const fetcher = (url: string) => api.get(url).then((res) => res.data);

function useTeam(endpoint: string) {
    const { data, error, isLoading } = useSWR(endpoint, fetcher);
    return { data, error, isLoading };
}

export default useTeam;
