import React, { useState, useEffect } from 'react';

const UserActivityTracker = () => {
    const [activeUsers, setActiveUsers] = useState(0);

    useEffect(() => {
        fetch('/useractivity')
            .then(response => response.json())
            .then(data => setActiveUsers(data.active_users));
    }, []);

    return (
        <div>
            <h2>Active Users</h2>
            <p>{activeUsers}</p>
        </div>
    );
};

export default UserActivityTracker;
