import { Button, Stack, TextField } from '@mui/material';
import QRCode from 'qrcode.react';
import { useRef, useState } from 'react';

const QRcodePage = () => {
  const [inputValue, setInputValue] = useState('');
  const [qrValue, setQrValue] = useState('');
  const qrRef = useRef();

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleGenerate = () => {
    setQrValue(inputValue);
  };

  const handleQRCodeDownload = () => {
    const canvas = qrRef.current.querySelector('canvas');
    const pngUrl = canvas.toDataURL('image/png').replace('image/png', 'image/octet-stream');
    const downloadLink = document.createElement('a');
    downloadLink.href = pngUrl;
    downloadLink.download = `${qrValue}.png`;
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
  };

  return (
    <>
      <h1>QR Code Generate</h1>
      <Stack direction={'column'} spacing={2}>
        <Stack direction={'row'} spacing={2}>
          <TextField type="text" value={inputValue} onChange={handleChange} size="small" />
          <Button variant="contained" onClick={handleGenerate}>
            Generate
          </Button>
        </Stack>
        {qrValue && (
          <div ref={qrRef}>
            <Stack direction={'column'} spacing={1}>
              <QRCode value={qrValue} />
              <Button variant="contained" color={'success'} onClick={handleQRCodeDownload} fullWidth={false} sx={{ width: '128px' }}>
                Download
              </Button>
            </Stack>
          </div>
        )}
      </Stack>
    </>
  );
};

export default QRcodePage;
