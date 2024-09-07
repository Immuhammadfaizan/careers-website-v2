import React, { useState } from 'react';

const SEOAnalyzer = () => {
    const [score, setScore] = useState(0);

    const analyzeSEO = () => {
        fetch('/seoanalyzer', { method: 'POST' })
            .then(response => response.json())
            .then(data => setScore(data.score));
    };

    return (
        <div>
            <h2>SEO Analyzer</h2>
            <button onClick={analyzeSEO}>Analyze</button>
            <p>Score: {score}</p>
        </div>
    );
};

export default SEOAnalyzer;
