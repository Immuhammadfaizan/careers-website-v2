import React, { useState } from 'react';

const KeywordResearch = () => {
    const [keywords, setKeywords] = useState([]);

    const fetchKeywords = () => {
        fetch('/keywordresearch', { method: 'POST' })
            .then(response => response.json())
            .then(data => setKeywords(data.keywords));
    };

    return (
        <div>
            <h2>Keyword Research</h2>
            <button onClick={fetchKeywords}>Get Keywords</button>
            <ul>
                {keywords.map((keyword, index) => (
                    <li key={index}>{keyword}</li>
                ))}
            </ul>
        </div>
    );
};

export default KeywordResearch;
