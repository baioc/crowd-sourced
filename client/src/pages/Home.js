import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Button } from '@material-ui/core';

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
    },
}));

export default function Home({ children }) {

    const classes = useStyles();

    return (
        <div className={classes.root}>
            <Button color="primary">Hello World</Button>
        </div>
    );
}