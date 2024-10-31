/* eslint-disable react/button-has-type */
function Button({
  children,
  onClick,
  type = 'button',
  variant = 'primary',
  disabled = false,
}) {
  const getButtonStyle = () => {
    switch (variant) {
      case 'primary':
        return 'bg-blue-500 hover:bg-blue-700 text-white'
      case 'secondary':
        return 'bg-gray-500 hover:bg-gray-700 text-white'
      case 'danger':
        return 'bg-red-500 hover:bg-red-700 text-white'
      default:
        return 'bg-blue-500 hover:bg-blue-700 text-white'
    }
  }

  return (
    <button
      type={type}
      onClick={onClick}
      className={`px-4 py-2 rounded ${getButtonStyle()} ${disabled ? 'opacity-50 cursor-not-allowed' : ''}`}
      disabled={disabled}
    >
      {children}
    </button>
  )
}

export default Button
