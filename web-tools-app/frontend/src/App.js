import React from 'react';
import PageViewCounter from './components/Analytics/PageViewCounter';
import UserActivityTracker from './components/Analytics/UserActivityTracker';
import MalwareScanner from './components/Security/MalwareScanner';
import SSLChecker from './components/Security/SSLChecker';
import SEOAnalyzer from './components/SEO/SEOAnalyzer';
import KeywordResearch from './components/SEO/KeywordResearch';
import SpeedTest from './components/Performance/SpeedTest';

const App = () => {
    return (
        <div>
            <h1>Web Tools App</h1>
            <PageViewCounter />
            <UserActivityTracker />
            <MalwareScanner />
            <SSLChecker />
            <SEOAnalyzer />
            <KeywordResearch />
            <SpeedTest />
        </div>
    );
};

export default App;
