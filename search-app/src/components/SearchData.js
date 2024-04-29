import React, { useState } from 'react';

export const API_URL="http://127.0.0.1:5000"

function SearchData() {
  const [searchText, setSearchText] = useState('');
  const [selectedOption, setSelectedOption] = useState('name');
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
   
  const handleSearch = async () => {
    if (searchText.trim() === '') {
      alert('Please enter a search term.');
      return;
    }

    setLoading(true);

    const response = await fetch(API_URL+"/api/v1/search", {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        dropdown: selectedOption,
        search: searchText
      })
    });

    const data = await response.json();

    // await new Promise(resolve => setTimeout(resolve, 2000));
    setResults(data);
    setLoading(false);
  };

  const handleDropdownChange = (e) => {
    setSelectedOption(e.target.value);
  };

  return (
    <div className='search-container'>
      <div className='search-bar'>
        <div>
          <input
            type="text"
            value={searchText}
            onChange={(e) => setSearchText(e.target.value)}
            placeholder="Enter search term"
          />
        </div>
        <div>
          <select value={selectedOption} onChange={handleDropdownChange}>
            <option value="Name">Name</option>
            <option value="Age">Age</option>
            <option value="City">City</option>
          </select>
        </div>
        <div>
          <button onClick={handleSearch}>Search</button>
        </div>
      </div>

      {loading ? (
        <div className="loader"></div>
      ) : (
        <div className={results ? "results-container" : ""}>
          {results &&
            Object.keys(results).map((key) => (
              <div key={key} className="result-category">
                <h3>{key}</h3>
                <div className="result-items">
                  {results[key].map((item, index) => (
                    <div key={index} className="result-item" style={{ animationDelay: `${index * 0.1}s` }}>
                      <p><strong>Name:</strong> {item.name}</p>
                      <p><strong>Age:</strong> {item.age}</p>
                      <p><strong>city:</strong> {item.city}</p>
                    </div>
                  ))}
                </div>
              </div>
            ))}
        </div>
      )}
    </div>
  );
}

export default SearchData;
