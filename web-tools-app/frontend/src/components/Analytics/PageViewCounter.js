import React, { useState, useEffect } from 'react';

const PageViewCounter = () => {
    const [views, setViews] = useState(0);

    useEffect(() => {
        fetch('/pageview')
            .then(response => response.json())
            .then(data => setViews(data.views));
    }, []);

    return (
        <div>
            <h2>Page Views</h2>
            <p>{views}</p>
        </div>
    );
};

export default PageViewCounter;
