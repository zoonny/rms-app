import { Button, MenuItem, Select, Stack, Typography } from '@mui/material';
import { Box } from '@mui/system';
import { useState } from 'react';
import { QrReader } from 'react-qr-reader';

const QRCodeScannerPage = () => {
  //   const [scanResult, setScanResult] = useState('');
  //   const handleScan = (data) => {
  //     if (data) {
  //       setScanResult(data);
  //       window.location.href = data; // Navigate to the scanned URL
  //     }
  //   };
  //   const handleError = (err) => {
  //     console.error(err);
  //   };
  //   return (
  //     <div className="App">
  //       <Typography variant="h1">QR Code Scanner</Typography>
  //       <Stack spacing={2} alignItems="center">
  //         <QrReader delay={300} onError={handleError} onScan={handleScan} style={{ width: '100%' }} />
  //         <Typography variant="body1">Scan a QR code to navigate to the URL</Typography>
  //         {scanResult && (
  //           <Typography variant="body2" color="textSecondary">
  //             Scanned URL: {scanResult}
  //           </Typography>
  //         )}
  //       </Stack>
  //     </div>
  //   );
  //   const [data, setData] = useState('No result');
  //   return (
  //     <>
  //       <p>{data}</p>
  //       <QrReader
  //         onResult={(result, error) => {
  //           if (!!result) {
  //             setData(result?.text);
  //           }
  //           if (!!error) {
  //             console.info(error);
  //           }
  //         }}
  //       />
  //     </>
  //   );

  const [selected, setSelected] = useState('environment');
  const [startScan, setStartScan] = useState(false);
  const [loadingScan, setLoadingScan] = useState(false);
  const [data, setData] = useState('');

  const handleResult = async (scanData) => {
    setLoadingScan(true);
    console.log(`loaded data data`, scanData);
    if (scanData && scanData !== '') {
      console.log(`loaded >>>`, scanData);
      setData(scanData);
      setStartScan(false);
      setLoadingScan(false);
      // setPrecScan(scanData);
    }
  };
  const handleError = (err) => {
    console.error(err);
  };

  return (
    <>
      <Stack spacing={2} direction={'column'} alignItems="left">
        <h2>
          Last Scan:
          {selected}
        </h2>
        <Button
          onClick={() => {
            setStartScan(!startScan);
          }}
        >
          {startScan ? 'Stop Scan' : 'Start Scan'}
        </Button>
        <Select onChange={(e) => setSelected(e.target.value)} value={selected}>
          <MenuItem value={'environment'}>Back Camera</MenuItem>
          <MenuItem value={'user'}>Front Camera</MenuItem>
        </Select>
      </Stack>
      {startScan && (
        <QrReader
          facingMode={selected}
          delay={1000}
          onError={handleError}
          onResult={handleResult}
          // chooseDeviceId={()=>selected}
          style={{ width: '300px' }}
        />
      )}
    </>
  );
};

export default QRCodeScannerPage;
