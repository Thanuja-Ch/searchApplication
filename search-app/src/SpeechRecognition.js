import React, { useState } from 'react';
import axios from 'axios';
import { saveAs } from 'file-saver';

const SpeechRecognition = () => {
  const [isRecording, setIsRecording] = useState(false);
  const [recordedText, setRecordedText] = useState('');
  const [recordings, setRecordings] = useState([]);
  const [recognition, setRecognition] = useState(null); // Added state for recognition instance
  const [recordingStatus, setRecordingStatus] = useState('Start Recording');
  const [showPreview, setShowPreview] = useState(false);

  const downloadExcel = async () => {
    try {
      const response = await axios.get('your-backend-excel-endpoint', {
        responseType: 'blob',
      });
      saveAs(response.data, 'speech_data.xlsx');
    } catch (error) {
      console.error('Error downloading Excel file:', error);
    }
  };

  const startRecording = () => {
    setIsRecording(true);
    setRecordingStatus('Stop Recording');
    const recognitionInstance = new window.webkitSpeechRecognition();
    recognitionInstance.lang = 'en-US';
    recognitionInstance.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      setRecordedText(transcript);
    };
    recognitionInstance.start();
    setRecognition(recognitionInstance);
  };

  const stopRecording = () => {
    setIsRecording(false);
    setRecordingStatus('Start Recording');
    recognition.stop();
  };

  const addRecording = () => {
    setRecordings((prevRecordings) => [...prevRecordings, recordedText]);
    setRecordedText('');
  };

  const tryAgain = () => {
    setRecordedText('');
    startRecording();
  };

  const togglePreview = () => {
    setShowPreview(!showPreview);
  };

  return (
    <div className='speech-recognition-container'>
      <div className="spch-container">
        <div className="centered">
          <div className="record-button-container">
            <button className={`record-button ${isRecording ? 'recording' : ''}`} onClick={isRecording ? stopRecording : startRecording}>
              {recordingStatus}
            </button>
            {recordedText && (
              <div className="recorded-text">
                <p>{recordedText}</p>
                <div className="button-container">
                  <button onClick={addRecording}>Add</button>
                  <button onClick={tryAgain}>Try Again</button>
                </div>
              </div>
            )}
          </div>
          <div className="save-preview-button-container">
            <button className="save-button" onClick={downloadExcel}>Save</button>
            <button className="preview-button" onClick={togglePreview}>Preview</button>
          </div>
        </div>
        {showPreview && (
          <div className="preview-container">
            <h2>Saved Recordings</h2>
            <ul>
              {recordings.map((recording, index) => (
                <li key={index}>{recording}</li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
};

export default SpeechRecognition;
