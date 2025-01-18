import React, { useState } from 'react';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import useTeam from './useTeam';

const ALL = 'ALL';

function TeamSelect() {
  const [selected, setSelected] = useState(ALL);
  const { data, error, isLoading } = useTeam(0, 10);

  if (error) return <div>Failed to load</div>;
  if (isLoading) return <div>Loading...</div>;

  const handleChange = (e) => {
    setSelected(e.target.value);
  };

  return (
    <FormControl fullWidth>
      <InputLabel id="demo-simple-select-label">팀</InputLabel>
      <Select labelId="demo-simple-select-label" id="demo-simple-select" value={selected || ALL} label="팀" onChange={handleChange}>
        <MenuItem key={ALL} value={ALL}>
          전체
        </MenuItem>
        {data &&
          data.map((item) => (
            <MenuItem key={item.id} value={item.id}>
              {item.name}
            </MenuItem>
          ))}
      </Select>
      {selected}
    </FormControl>
  );
}

export default TeamSelect;
