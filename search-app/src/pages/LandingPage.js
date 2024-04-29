import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import SimpleInterest from '../components/SimpleInterest';
import SpeechRecognition from '../components/SpeechRecognition';
import SearchData from '../components/SearchData';

const App = () => {
  return (
    <Router>
      <div className='landing_page_container'>
        <div className='landing_page_nav_bar'>
          <div className='tasks'>
            <Link className='links' to="/search">Search Data</Link>
          </div>
          <div className='tasks'>
            <Link className='links' to="/interest">Interest Calculator</Link>
          </div>
          <div className='tasks'>
            <Link className='links' to="/recognition">Speech Recognition</Link>
          </div>
        </div>

        <div className='tasks-container'>
          <Routes>
            <Route path="/search" element={<SearchData />} />
            <Route path="/interest" element={<SimpleInterest />} />
            <Route path="/recognition" element={<SpeechRecognition />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
