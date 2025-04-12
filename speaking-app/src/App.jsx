import React, { useState } from 'react';
import { UploadCloud } from 'lucide-react';
import './App.css'; // make sure this import is here

export default function App() {
  const [videoFile, setVideoFile] = useState(null);

  const handleUpload = (event) => {
    const file = event.target.files[0];
    if (file && file.type.startsWith('video/')) {
      setVideoFile(file);
    } else {
      alert('Please upload a valid video file.');
    }
  };

  return (
    <div className="app-container">
      <div className="upload-box">
        <h1>Upload a Video Clip</h1>
        <label htmlFor="video-upload" className="upload-label">
          <UploadCloud size={40} />
          <span>Click to upload a video</span>
          <input
            id="video-upload"
            type="file"
            accept="video/*"
            className="hidden-input"
            onChange={handleUpload}
          />
        </label>

        {videoFile && (
          <div className="file-info">
            <p><strong>Selected file:</strong></p>
            <p>{videoFile.name}</p>
          </div>
        )}

        {videoFile && (
          <button className="analyze-button">Analyze Video</button>
        )}
      </div>
    </div>
  );
}
