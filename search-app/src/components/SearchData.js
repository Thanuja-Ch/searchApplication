import React, { useState } from 'react';

export const API_URL="http://localhost:5000"

function SearchData() {
  const [searchText, setSearchText] = useState('');
  const [selectedOption, setSelectedOption] = useState('default');
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false); // State for loader

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
        dropdownValue: selectedOption,
        searchText: searchText
      })
    });

    const data = await response.json();
    console.log(data)
//     const data = {
//       "users": [
//           {"name": "Alice", "email": "alice@example.com"},
//           {"name": "Bob", "email": "bob@example.com"},
//           {"name": "Charlie", "email": "charlie@example.com"},
//           {"name": "David", "email": "david@example.com"}
//       ],
//       "employees": [
//           {"name": "Emily", "email": "emily@example.com"},
//           {"name": "Frank", "email": "frank@example.com"},
//           {"name": "Grace", "email": "grace@example.com"}
//       ]
//   }
  
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
            <option value="default" disabled>Select an option</option>
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
                      <p><strong>Email:</strong> {item.email}</p>
                      <p><strong>Email1:</strong> ''</p>
                      <p><strong>Email1:</strong> ''</p>
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
