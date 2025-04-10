import React, { useState } from 'react';

function ReceiptUpload() {
  const [receipt, setReceipt] = useState(null);
  const [receiptData, setReceiptData] = useState(null);

  const handleFileChange = (event) => {
    setReceipt(event.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('receipt', receipt);

    try {
      const response = await fetch('http://127.0.0.1:5000/api/process_receipt', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Failed to upload receipt');
      }

      const data = await response.json();
      setReceiptData(data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h2>Upload Receipt</h2>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>

      {receiptData && (
        <div>
          <h3>Receipt Data:</h3>
          <pre>{JSON.stringify(receiptData, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default ReceiptUpload;
