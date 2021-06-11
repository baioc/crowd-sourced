import { makeStyles, Grid, Paper } from '@material-ui/core';
import React from 'react';

// Local imports
import CardForDisplay from './CardForDisplay';

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
        width: '100%'
    },
    paper: {
        padding: theme.spacing(2),
        textAlign: 'center',
        color: theme.palette.text.secondary,
        width: 'inherit'
    },
    occupy: {
        width: 'inherit',
    }
}));

export const ToLabelContainer = () => {

    const classes = useStyles();

    return (
        <div className={classes.root}>
            <Grid container direction="column"
                justify="center"
                alignItems="center">
                <Grid item xs={12} className={classes.occupy}>
                    <Paper className={classes.paper}>
                        <CardForDisplay />
                    </Paper>
                </Grid>
            </Grid>
        </div>
    )

}