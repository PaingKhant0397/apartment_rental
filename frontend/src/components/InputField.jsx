/* eslint-disable react/no-array-index-key */
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
      <textarea
        id={id}
        name={id}
        value={value}
        onChange={onChange}
        className={`mt-1 block w-full px-3 py-2 border ${
          error ? 'border-red-500' : 'border-gray-300'
        } rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm`}
        required={required}
        rows={5}
      />
    )
  } else if (type === 'file') {
    inputElement = (
      <input
        type='file'
        id={id}
        name={id}
        onChange={onChange}
        className={`mt-1 block w-full px-3 py-2 border ${
          error ? 'border-red-500' : 'border-gray-300'
        } rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm`}
        required={required}
      />
    )
  } else if (type === 'select') {
    inputElement = (
      <select
        id={id}
        name={id}
        value={value}
        onChange={onChange}
        className={`mt-1 block w-full px-3 py-2 border ${
          error ? 'border-red-500' : 'border-gray-300'
        } rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm`}
        required={required}
      >
        <option value='' disabled>
          Select an option
        </option>
        {options.map((option, index) => (
          <option key={index} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
    )
  } else {
    inputElement = (
      <input
        type={type}
        id={id}
        name={id}
        value={value}
        onChange={onChange}
        className={`mt-1 block w-full px-3 py-2 border ${
          error ? 'border-red-500' : 'border-gray-300'
        } rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm`}
        required={required}
      />
    )
  }

  return (
    <div className='mb-4'>
      <label htmlFor={id} className='block text-sm font-medium text-gray-700'>
        {label}
      </label>
      {inputElement}
      {error && <p className='text-red-500 text-sm'>{error}</p>}
    </div>
  )
}

export default InputField
