import { Box, Button } from '@mui/material';
import Typography from '@mui/material/Typography';
import { Stack } from '@mui/system';
import { DataGrid } from '@mui/x-data-grid';

// project import
import MainCard from 'components/MainCard';
import StyledDataGrid, { CustomPagination } from 'components/StyledDataGrid';
import { useState } from 'react';
import { create } from 'zustand';

// ==============================|| SAMPLE PAGE ||============================== //

const columns = [
  { field: 'id', headerName: 'ID', width: 90 },
  {
    field: 'firstName',
    headerName: 'First name',
    width: 150,
    editable: true,
    headerClassName: 'super-app-theme--header'
  },
  {
    field: 'lastName',
    headerName: 'Last name',
    width: 150,
    editable: true
  },
  {
    field: 'age',
    headerName: 'Age',
    type: 'number',
    width: 110,
    editable: true
  },
  {
    field: 'fullName',
    headerName: 'Full name',
    description: 'This column has a value getter and is not sortable.',
    sortable: false,
    width: 160,
    valueGetter: (value, row) => `${row.firstName || ''} ${row.lastName || ''}`
  }
];

const rows = [
  { id: 1, lastName: 'Snow', firstName: 'Jon', age: 14 },
  { id: 2, lastName: 'Lannister', firstName: 'Cersei', age: 31 },
  { id: 3, lastName: 'Lannister', firstName: 'Jaime', age: 31 },
  { id: 4, lastName: 'Stark', firstName: 'Arya', age: 11 },
  { id: 5, lastName: 'Targaryen', firstName: 'Daenerys', age: null },
  { id: 6, lastName: 'Melisandre', firstName: null, age: 150 },
  { id: 7, lastName: 'Clifford', firstName: 'Ferrara', age: 44 },
  { id: 8, lastName: 'Frances', firstName: 'Rossini', age: 36 },
  { id: 9, lastName: 'Roxie', firstName: 'Harvey', age: 65 }
];

const useBearStore = create((set) => ({
  bears: 0,
  increasePopulation: () => set((state) => ({ bears: state.bears + 1 })),
  removeAllBears: () => set({ bears: 0 })
}));

export default function SamplePage() {
  const [paginationModel, setPaginationModel] = useState({
    pageSize: 5,
    page: 0
  });
  const { bears, increasePopulation, removeAllBears } = useBearStore((state) => state);
  return (
    <Stack direction={'column'} spacing={2}>
      <MainCard title="Button">
        <div>{bears}</div>
        <Stack direction={'row'} spacing={1}>
          <Button
            variant="contained"
            onClick={(e) => {
              increasePopulation();
            }}
          >
            Primary
          </Button>
          <Button variant="contained" color="secondary" onClick={removeAllBears}>
            Secondary
          </Button>
          <Button variant="contained" color="info">
            Info
          </Button>
          <Button variant="contained" color="success">
            Success
          </Button>
          <Button variant="contained" color="warning">
            Warning
          </Button>
          <Button variant="contained" color="error">
            Error
          </Button>
        </Stack>
      </MainCard>
      {/* <MainCard title="Data Grid">
        <DataGrid
          sx={{
            boxShadow: 2,
            border: 2,
            borderColor: 'primary.light',
            '& .MuiDataGrid-cell:hover': {
              color: 'primary.main'
            },
            fontSize: '0.75rem'
            // '& .super-app-theme--header': {
            //   backgroundColor: 'rgba(255, 7, 0, 0.55)'
            // }
          }}
          autoHeight
          rows={rows}
          columns={columns}
          initialState={{
            density: 'compact',
            pagination: {
              paginationModel: {
                pageSize: 5
              }
            }
          }}
          pageSizeOptions={[5]}
          checkboxSelection
          disableRowSelectionOnClick
        />
      </MainCard> */}
      <MainCard title="Styled Data Grid">
        <StyledDataGrid
          checkboxSelection
          paginationModel={paginationModel}
          onPaginationModelChange={setPaginationModel}
          pageSizeOptions={[5]}
          slots={{
            pagination: CustomPagination
          }}
          initialState={{
            density: 'compact'
          }}
          rows={rows}
          columns={columns}
        />
      </MainCard>
      <MainCard title="Sample Card">
        <Typography variant="body2">
          Lorem ipsum dolor sit amen, consenter nipissing eli, sed do elusion tempos incident ut laborers et doolie magna alissa. Ut enif ad
          minim venice, quin nostrum exercitation illampu laborings nisi ut liquid ex ea commons construal. Duos aube grue dolor in
          reprehended in voltage veil esse colum doolie eu fujian bulla parian. Exceptive sin ocean cuspidate non president, sunk in culpa
          qui officiate descent molls anim id est labours.
        </Typography>
      </MainCard>
    </Stack>
  );
}
