import React from 'react';
import clsx from 'clsx';
import {
    Grid,
    makeStyles,
    FormLabel,
    FormControl,
    FormControlLabel,
    RadioGroup,
    Radio,
    Button
} from '@material-ui/core';

// Local imports
import { TextHeader } from '../TextHeader';
import { ToLabelContainer } from '../ToLabelContainer';

const useStyles = makeStyles((theme) => ({
    root: {
        '& > *': {
            margin: theme.spacing(1),
        },
        '&:hover': {
            backgroundColor: 'transparent',
        },
    },
    icon: {
        borderRadius: '50%',
        width: 16,
        height: 16,
        boxShadow: 'inset 0 0 0 1px rgba(16,22,26,.2), inset 0 -1px 0 rgba(16,22,26,.1)',
        backgroundColor: '#f5f8fa',
        backgroundImage: 'linear-gradient(180deg,hsla(0,0%,100%,.8),hsla(0,0%,100%,0))',
        '$root.Mui-focusVisible &': {
            outline: '2px auto rgba(19,124,189,.6)',
            outlineOffset: 2,
        },
        'input:hover ~ &': {
            backgroundColor: '#ebf1f5',
        },
        'input:disabled ~ &': {
            boxShadow: 'none',
            background: 'rgba(206,217,224,.5)',
        },
    },
    checkedIcon: {
        backgroundColor: '#137cbd',
        backgroundImage: 'linear-gradient(180deg,hsla(0,0%,100%,.1),hsla(0,0%,100%,0))',
        '&:before': {
            display: 'block',
            width: 16,
            height: 16,
            backgroundImage: 'radial-gradient(#fff,#fff 28%,transparent 32%)',
            content: '""',
        },
        'input:hover ~ &': {
            backgroundColor: '#106ba3',
        },
    },
    spacing: {
        marginTop: '10px',
    },
    button: {
        margin: '10px',
    },
}));

// Inspired by blueprintjs
function StyledRadio(props) {
    const classes = useStyles();

    return (
        <Radio
            className={classes.root}
            disableRipple
            color="default"
            checkedIcon={<span className={clsx(classes.icon, classes.checkedIcon)} />}
            icon={<span className={classes.icon} />}
            {...props}
        />
    );
};

export const ComponentGrid = (() => {

    const classes = useStyles();
    const [value, setValue] = React.useState('female');

    const handleChange = (event) => {
        setValue(event.target.value);
    };

    return (
        <div className={classes.root}>
            <Grid container
                direction="column"
                justify="center"
                alignItems="stretch"
                spacing={2}
            >
                <Grid item xs={12}>
                    <TextHeader header={'Please select the option that better describes this image'} text={'OpenImages Classification'} linkTo={'http://kaggle.com/'} />
                </Grid>
                <Grid item xs={12}>
                    <Grid container direction='row' justify='center' spacing={2}>
                        <Grid item>
                            <ToLabelContainer />
                        </Grid>
                    </Grid>
                </Grid>
                <Grid item xs={12} className={classes.spacing}>
                    <Grid container spacing={3} direction="column"
                        justify="center"
                        alignItems="center">
                        <FormControl component="fieldset">
                            <FormLabel component="legend">Options</FormLabel>
                            <RadioGroup aria-label="options" name="options_1" value={value} onChange={handleChange}>
                                <Grid container direction='row' justify='center' spacing={2}>
                                    <Grid item xs={6}>
                                        <FormControlLabel value="cat" control={<StyledRadio />} label="Cat" />
                                    </Grid>
                                    <Grid item xs={6}>
                                        <FormControlLabel value="dog" control={<StyledRadio />} label="Dog" />
                                    </Grid>
                                    <Grid item xs={6}>
                                        <FormControlLabel value="person" control={<StyledRadio />} label="Person" />
                                    </Grid>
                                    <Grid item xs={6}>
                                        <FormControlLabel value="bird" control={<StyledRadio />} label="Bird" />
                                    </Grid>
                                </Grid>
                            </RadioGroup>
                        </FormControl>
                    </Grid>
                </Grid>
                <Grid item xs={12} className={classes.button}>
                    <Grid container spacing={3} direction="column"
                        justify="flex-end"
                        alignItems="center">
                        <Button variant="contained">Submit!</Button>
                    </Grid>
                </Grid>
            </Grid>
        </div>
    );
});