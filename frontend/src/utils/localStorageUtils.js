// Utility function to set a Item in localStorage
export function setItem(ItemName, ItemValue) {
  try {
    localStorage.setItem(ItemName, ItemValue)
  } catch (error) {
    console.error('Error setting Item in localStorage', error)
  }
}

// Utility function to get a Item from localStorage
export function getItem(ItemName) {
  try {
    return localStorage.getItem(ItemName)
  } catch (error) {
    console.error('Error getting Item from localStorage', error)
    return null
  }
}

// Utility function to remove a Item from localStorage
export function removeItem(ItemName) {
  try {
    localStorage.removeItem(ItemName)
  } catch (error) {
    console.error('Error removing Item from localStorage', error)
  }
}

// Utility function to update an existing Item in localStorage
export function updateItem(ItemName, newItemValue) {
  try {
    if (localStorage.getItem(ItemName)) {
      localStorage.setItem(ItemName, newItemValue)
    } else {
      console.warn('Item does not exist in localStorage')
    }
  } catch (error) {
    console.error('Error updating Item in localStorage', error)
  }
}

// Utility function to clear all Items from localStorage (optional)
export function clearAllItems() {
  try {
    localStorage.clear()
  } catch (error) {
    console.error('Error clearing localStorage', error)
  }
}
