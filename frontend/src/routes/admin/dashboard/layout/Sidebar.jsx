/* eslint-disable react/no-array-index-key */

import { NavLink } from 'react-router-dom'

export default function Sidebar() {
  const navLinkList = [
    {
      name: 'Home',
      to: '/admin/dashboard',
    },
    {
      name: 'Apartment Register',
      to: '/admin/dashboard/apartments/register',
    },
    {
      name: 'Apartment List',
      to: '/admin/dashboard/apartments/',
    },
  ]
  return (
    <aside className='w-64 min-h-screen bg-gray-800 text-white'>
      <div className='p-4'>
        <h1 className='text-2xl font-bold'>Admin Dashboard</h1>
      </div>
      <nav className='mt-8 px-2'>
        <ul>
          {navLinkList.map((navLink, index) => (
            <li className='mb-4' key={index}>
              <NavLink
                to={navLink.to}
                className={({ isActive }) =>
                  `block px-4 py-2 hover:bg-gray-700 rounded ${isActive ? 'bg-gray-700' : ''}`
                }
                end
              >
                {navLink.name}
              </NavLink>
            </li>
          ))}
        </ul>
      </nav>
    </aside>
  )
}
