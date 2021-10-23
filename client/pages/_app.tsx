import '../styles/globals.css'
import type { AppProps } from 'next/app'
import { StylesProvider, createGenerateClassName } from '@mui/styles'
const generateClassName = createGenerateClassName({
  productionPrefix: 'c',
})
function MyApp({ Component, pageProps }: AppProps) {
  return (
    <StylesProvider generateClassName={generateClassName}>
      <Component {...pageProps} />
    </StylesProvider>
  )
}
export default MyApp
