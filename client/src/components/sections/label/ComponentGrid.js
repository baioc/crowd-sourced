import React from 'react';
import { Grid, makeStyles } from '@material-ui/core';

// Local imports
import { TextHeader } from '../TextHeader';
import { ToLabelContainer } from '../ToLabelContainer';
import { FormSubmit } from '../FormSubmit';

const useStyles = makeStyles((theme) => ({
    root: {
        '& > *': {
            margin: theme.spacing(1),
        }, 
    },
}));

export const ComponentGrid = (() => {

    const classes = useStyles();

    return (
        <div className={classes.root}>
            <Grid container
                direction="column"
                justify="center"
                alignItems="center"
                spacing={2}
            >
                <Grid item xs={12}>
                    <TextHeader header={'Please enter the letters and numbers you see below'} text={'Street View Numbers'} linkTo={'http://kaggle.com/'} />
                </Grid>
                <Grid item xs={12}>
                    <ToLabelContainer />
                </Grid>
                <Grid item xs={12}>
                    <FormSubmit
                        formName="Your Answer"
                        formDescription="Click 'submit' to store answer"
                    />
                </Grid>
            </Grid>
        </div>
    );
});