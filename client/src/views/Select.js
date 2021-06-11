import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Grid } from '@material-ui/core';

import Bar from './Bar';

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
        margin: 0,
    },
    menuButton: {
        marginRight: theme.spacing(2),
    },
    title: {
        flexGrow: 1,
    },
    bottomNavBar: {
        width: 500, 
    },
    gridSizing: {
        width: '100%',
        height: '100%',
        margin: 0,
        padding: 0
    },
    centerBar: {
        height: '80vh',
    }
}));

export default function Select({ children }) {
    const classes = useStyles();

    return (
        <Grid container direction="column" justify="space-between" alignItems="stretch" className={classes.root} >
            <Grid item className={`${classes.gridSizing} ${classes.topBar}`} container direction='row' alignItems='flex-end' justify='center'>
                <Bar content={"Train Crowd-Sourced"} />
            </Grid>
            <Grid item className={`${classes.gridSizing} ${classes.centerBar}`} container direction='row' alignItems='center' justify='center'>
                Here!
                </Grid>
            <Grid item className={`${classes.gridSizing} ${classes.bottomBar}`} container direction='row' alignItems='flex-end' justify='center'>
                <Bar content={"Find this on GitHub, at baio/crowd-sourced!"}/>
            </Grid>

        </Grid>
    );
}