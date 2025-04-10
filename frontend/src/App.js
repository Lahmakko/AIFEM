import { useState } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("");
  const [file, setFile] = useState(null);

  // Handle file selection
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  // Handle form submission to send the file to the backend
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file) {
      setMessage("Please upload a receipt.");
      return;
    }

    const formData = new FormData();
    formData.append("receipt", file);

    try {
      const response = await axios.post("http://localhost:5000/api/process_receipt", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      setMessage(JSON.stringify(response.data, null, 2));
    } catch (error) {
      setMessage("Error processing receipt.");
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Receipt Upload</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Upload Receipt</button>
      </form>
      <pre>{message}</pre>
    </div>
  );
}

export default App;
