import { Button, Input, Stack, Typography } from '@mui/material';
import MainCard from 'components/MainCard';
import useSWR from 'swr';
import usePost from './usePost';
import { create } from 'zustand';

// const Card1 = () => {
//   const fetcher = (...args) => fetch(...args).then((response) => response.json());
//   const { data, error, isLoading } = useSWR(`${ROOT_URL}/posts/1`, fetcher);

//   if (error) return <div>Failed to load</div>;
//   if (isLoading) return <div>Loading...</div>;

//   return (
//     <MainCard title="Post">
//       <h2>{data.title}</h2>
//       <Typography>{data.body}</Typography>
//     </MainCard>
//   );
// };

// const store = create((set) => ({
//   posts: [],
//   addPost: (post) => set((state) => ({ posts: [...state.posts, post] }))
// }));

// const useStore = create(() => ({
//   like: 0
// }));

const useStore = create((set) => ({
  like: 0,
  increaseLike: () => set((state) => ({ like: state.like + 1 })),
  decreaseLike: (unlike) => set((state) => ({ like: state.like - unlike }))
}));

const Card1 = () => {
  const { post, error, isLoading } = usePost(1);
  const like = useStore((state) => state.like);

  if (error) return <div>Failed to load</div>;
  if (isLoading) return <div>Loading...</div>;

  return (
    <MainCard title="Post">
      <h2>{post.title}</h2>
      <Typography gutterBottom>{post.body}</Typography>
      <Typography variant="caption" display="block" gutterBottom>
        {like}
      </Typography>
      <Button onClick={() => useStore.setState({ like: like + 1 })}>Like</Button>
    </MainCard>
  );
};

const Card2 = () => {
  const { post, error, isLoading } = usePost(1);
  const { like, decreaseLike } = useStore((state) => state);

  if (error) return <div>Failed to load</div>;
  if (isLoading) return <div>Loading...</div>;

  return (
    <MainCard title="Post">
      <h2>{post.title}</h2>
      <Typography>{post.body}</Typography>
      <Typography variant="caption" display="block" gutterBottom>
        {like}
      </Typography>
      <Button onClick={() => decreaseLike(2)}>Unlike</Button>
    </MainCard>
  );
};

const PlayPage = () => {
  return (
    <Stack direction={'column'} spacing={2}>
      <Card1 />
      <Card2 />
    </Stack>
  );
};

export default PlayPage;
