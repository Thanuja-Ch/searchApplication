import React, { useState } from 'react';

export const API_URL="http://127.0.0.1:5000"

const SimpleInterest = () => {
    const [formData, setFormData] = useState({
        principal: '',
        rate: '',
        time: '',
    });
    const [response, setResponse] = useState('');
    const [isSubmitDisabled, setIsSubmitDisabled] = useState(true);
    const [loading, setLoading] = useState(false);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value,
        }));
        setIsSubmitDisabled(
            !Object.values({ ...formData, [name]: value }).every((val) => val.trim() !== '')
        );
    };


    const handleSubmit = async (e) => {
        e.preventDefault();
            setLoading(true);
            const response = await fetch(API_URL+"/api/v1/interest-calculator", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });
            const responseData = await response.json();
            

            // await new Promise(resolve => setTimeout(resolve, 2000));
            setResponse(responseData.interest);
            setLoading(false);
        
    };

    return (
        <div className='frag-container'>
            <div className="container">
                <form className="form" onSubmit={handleSubmit}>
                    <label className="input-label">
                        Principal:
                        <input className="input-field" type="number" name="principal" value={formData.principal} onChange={handleChange} />
                    </label>
                    <br />
                    <label className="input-label">
                        Rate Of Interest:
                        <input className="input-field" type="number" name="rate" value={formData.rate} onChange={handleChange} />
                    </label>
                    <br />
                    <label className="input-label">
                        Tenure:
                        <input className="input-field" type="number" name="time" value={formData.time} onChange={handleChange} />
                    </label>
                    <br />
                    <button className={isSubmitDisabled ? 'disabledButton' : "submit-btn"} type="submit" disabled={isSubmitDisabled}>Submit</button>
                </form>
            </div>
            {loading? (<div className="loader"></div>): (<div className='response'>
                {response && <div className="response-text">Total Interest: {response}</div>}
            </div>)}
            
        </div>
    );
};

export default SimpleInterest;

