import React from 'react';
import { DataGrid } from '@mui/x-data-grid';
// import { useDemoData } from '@mui/x-data-grid-generator';
import useProject from './useProject';
import dateFormat from 'utils/dateFormat';

const columns = [
  { field: 'id', headerName: 'ID', width: 70 },
  { field: 'name', headerName: 'Name', width: 130 },
  {
    field: 'start_date',
    headerName: 'Start Date',
    width: 130,
    valueFormatter: (value) => dateFormat(value)
  },
  { field: 'end_date', headerName: 'End Date', width: 130, valueFormatter: (value) => dateFormat(value) },
  {
    field: 'from-to',
    headerName: 'From To',
    description: 'This column has a value getter and is not sortable.',
    sortable: false,
    width: 280,
    valueGetter: (value, row) => `${row.start_date || ''} ~ ${row.end_date || ''}`
  }
];

function ProjectsTable() {
  const { data, error, isLoading } = useProject(0, 10);

  if (error) return <div>Failed to load</div>;
  if (isLoading) return <div>Loading...</div>;

  return (
    <div style={{ height: 400, width: '100%' }}>
      <div style={{ display: 'flex', height: '100%' }}>
        <div style={{ flexGrow: 1 }}>
          <DataGrid rows={data} columns={columns} pageSize={5} rowsPerPageOptions={[5]} checkboxSelection />
        </div>
      </div>
    </div>
  );
}

export default ProjectsTable;
