import React from 'react'
import {
  TextField,
  MenuItem,
  InputLabel,
  Select,
  FormControl,
  FormHelperText,
} from '@mui/material'

function InputField({
  id,
  label,
  type,
  value,
  onChange,
  error,
  required,
  options = [],
}) {
  let inputElement

  if (type === 'textarea') {
    inputElement = (
      <TextField
        id={id}
        name={id}
        label={label}
        value={value}
        onChange={onChange}
        variant='outlined'
        fullWidth
        multiline
        rows={5}
        required={required}
        error={!!error}
        helperText={error}
        InputLabelProps={{
          shrink: true, // Ensure the label stays above the textarea
        }}
        sx={{
          '& .MuiOutlinedInput-root': {
            '& fieldset': {
              borderColor: error ? 'red' : 'gray', // Customize border color on error
            },
          },
        }}
      />
    )
  } else if (type === 'file') {
    inputElement = (
      <TextField
        type='file'
        id={id}
        name={id}
        onChange={onChange}
        variant='outlined'
        fullWidth
        required={required}
        error={!!error}
        helperText={error}
        InputLabelProps={{
          shrink: true,
        }}
      />
    )
  } else if (type === 'select') {
    inputElement = (
      <FormControl
        fullWidth
        variant='outlined'
        required={required}
        error={!!error}
      >
        <InputLabel id={`${id}-label`}>{label}</InputLabel>
        <Select
          labelId={`${id}-label`}
          id={id}
          name={id}
          value={value}
          onChange={onChange}
          label={label}
        >
          <MenuItem value='' disabled>
            Select an option
          </MenuItem>
          {options.map((option, index) => (
            <MenuItem key={index} value={option.value}>
              {option.label}
            </MenuItem>
          ))}
        </Select>
        {error && <FormHelperText>{error}</FormHelperText>}
      </FormControl>
    )
  } else {
    inputElement = (
      <TextField
        type={type}
        id={id}
        name={id}
        label={label}
        value={value}
        onChange={onChange}
        variant='outlined'
        fullWidth
        required={required}
        error={!!error}
        helperText={error}
        InputLabelProps={type === 'date' ? { shrink: true } : {}}
        placeholder={type === 'date' ? 'dd/mm/yyyy' : ''}
      />
    )
  }

  return <div style={{ marginBottom: '1rem' }}>{inputElement}</div>
}

export default InputField
