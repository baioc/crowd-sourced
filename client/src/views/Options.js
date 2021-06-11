import React from 'react';
import { Grid, makeStyles } from '@material-ui/core';

import Bar from './Bar';
import { ComponentGrid } from '../components/sections/options/ComponentGrid';

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

export default function Options({ children }) {
    const classes = useStyles();

    return (
        <Grid container direction="column" justify="space-between" alignItems="stretch" className={classes.root} >
            <Grid item className={`${classes.gridSizing} ${classes.topBar}`} container direction='row' alignItems='flex-end' justify='center'>
                <Bar content={"Train Crowd-Sourced"} />
            </Grid>
            <Grid item className={`${classes.gridSizing} ${classes.centerBar}`} container direction='row' alignItems='center' justify='center'>
                <ComponentGrid />
            </Grid>
            <Grid item className={`${classes.gridSizing} ${classes.bottomBar}`} container direction='row' alignItems='flex-end' justify='center'>
                <Bar content={"Find this on GitHub, at baio/crowd-sourced!"} />
            </Grid>

        </Grid>
    );
}