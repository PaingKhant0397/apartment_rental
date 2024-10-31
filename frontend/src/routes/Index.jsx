import { Outlet } from 'react-router-dom'
import Header from './layout/Header'
import Footer from './layout/Footer'

export default function Index() {
  return (
    <>
      <Header />
      <main className='bg-slate-100 pt-2 pb-6'>
        <Outlet />
      </main>
      <Footer />
    </>
  )
}
