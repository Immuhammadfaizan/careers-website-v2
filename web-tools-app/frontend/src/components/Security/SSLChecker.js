import React, { useState, useEffect } from 'react';

const SSLChecker = () => {
    const [status, setStatus] = useState('');

    useEffect(() => {
        fetch('/sslchecker')
            .then(response => response.json())
            .then(data => setStatus(data.status));
    }, []);

    return (
        <div>
            <h2>SSL Checker</h2>
            <p>{status}</p>
        </div>
    );
};

export default SSLChecker;
