import React from 'react';
import { useRoutes } from 'react-router-dom';
import { ThemeProvider } from '@material-ui/core';
import routes from './routes';

const App = () => {
  const routing = useRoutes(routes);

  return (
    <ThemeProvider>
      {routing}
    </ThemeProvider>
  );
};

export default App;
