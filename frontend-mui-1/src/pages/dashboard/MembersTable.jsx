import React from 'react';
import { DataGrid } from '@mui/x-data-grid';
import useMember from './useMember';
import dateFormat from 'utils/dateFormat';

const columns = [
  { field: 'id', headerName: '사번', width: 130 },
  { field: 'employee_id', headerName: '2사번', width: 130 },
  { field: 'name', headerName: '이름', width: 130 },
  { field: 'position', headerName: '직급', width: 130 }
  // {
  //   field: 'start_date',
  //   headerName: 'Start Date',
  //   width: 130,
  //   valueFormatter: (value) => dateFormat(value)
  // },
  // { field: 'end_date', headerName: 'End Date', width: 130, valueFormatter: (value) => dateFormat(value) },
  // {
  //   field: 'from-to',
  //   headerName: 'From To',
  //   description: 'This column has a value getter and is not sortable.',
  //   sortable: false,
  //   width: 280,
  //   valueGetter: (value, row) => `${row.start_date || ''} ~ ${row.end_date || ''}`
  // }
];

function MembersTable() {
  const { data, error, isLoading } = useMember(0, 10);

  if (error) return <div>Failed to load</div>;
  if (isLoading) return <div>Loading...</div>;

  return (
    <div style={{ height: 400, width: '100%' }}>
      <div style={{ display: 'flex', height: '100%' }}>
        <div style={{ flexGrow: 1 }}>
          <DataGrid rows={data} columns={columns} pageSize={5} rowsPerPageOptions={[5]} />
        </div>
      </div>
    </div>
  );
}

export default MembersTable;
