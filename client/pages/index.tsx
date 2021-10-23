import type { NextPage } from 'next'
import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import useSWR from 'swr'
import axios from 'axios'
import React, { useEffect, useState } from 'react'
import { Button, CssBaseline, NoSsr } from '@mui/material'
import {
  DataGrid,
  GridColDef,
  GridValueGetterParams,
} from '@material-ui/data-grid'

import { createTheme, darken, lighten } from '@mui/material/styles'
import { makeStyles } from '@mui/styles'
const defaultTheme = createTheme()
const useStyles = makeStyles(
  (theme) => {
    const getBackgroundColor = (color: string) =>
      theme.palette.mode === 'dark' ? darken(color, 0.6) : lighten(color, 0.6)

    const getHoverBackgroundColor = (color: string) =>
      theme.palette.mode === 'dark' ? darken(color, 0.5) : lighten(color, 0.5)

    return {
      root: {
        '& .super-app-theme--yes': {
          backgroundColor: getBackgroundColor(theme.palette.info.main),
          '&:hover': {
            backgroundColor: getHoverBackgroundColor(theme.palette.info.main),
          },
        },
        '& .super-app-theme--no': {
          backgroundColor: getBackgroundColor(theme.palette.error.main),
          '&:hover': {
            backgroundColor: getHoverBackgroundColor(theme.palette.error.main),
          },
        },
        '& .super-app-theme--Snoww': {
          backgroundColor: getBackgroundColor(theme.palette.info.main),
          '&:hover': {
            backgroundColor: getHoverBackgroundColor(theme.palette.info.main),
          },
        },
        '& .super-app-theme--Snow': {
          backgroundColor: getBackgroundColor(theme.palette.success.main),
          '&:hover': {
            backgroundColor: getHoverBackgroundColor(
              theme.palette.success.main
            ),
          },
        },
        '& .super-app-theme--PartiallyFilled': {
          backgroundColor: getBackgroundColor(theme.palette.warning.main),
          '&:hover': {
            backgroundColor: getHoverBackgroundColor(
              theme.palette.warning.main
            ),
          },
        },
        '& .super-app-theme--Rejected': {
          backgroundColor: getBackgroundColor(theme.palette.error.main),
          '&:hover': {
            backgroundColor: getHoverBackgroundColor(theme.palette.error.main),
          },
        },
      },
    }
  },
  { defaultTheme }
)

const columns: GridColDef[] = [
  { field: 'id', headerName: 'ID', width: 150 },
  {
    field: 'correctness',
    headerName: 'Correctness',
    type: 'number',
    width: 150,
  },
  {
    field: 'sex',
    headerName: 'Sex',
    width: 150,
  },
  {
    field: 'maritalStatus',
    headerName: 'Marital Status',
    width: 150,
  },
  {
    field: 'education',
    headerName: 'Education',
    width: 110,
  },
  {
    field: 'category',
    headerName: 'Category',
    width: 110,
  },
  {
    field: 'debitAmount',
    headerName: 'DebitAmount',
    type: 'number',
    width: 110,
  },
  {
    field: 'monthOfOperation',
    headerName: 'MonthOfOperation',
    type: 'number',
    width: 110,
  },
  {
    field: 'age',
    headerName: 'Age',
    type: 'number',
    width: 110,
  },
  {
    field: 'accountAge',
    headerName: 'AccountAge',
    type: 'number',
    width: 110,
  },
]

// const rows = [{ id: 1, maritalStatus: 'Snow', firstName: 'Jon', education: 35 }]

interface Response {
  money: number
}

const config = {
  headers: { Authorization: `Bearer 2e36f199-bf00-30ba-a8a8-0618263101e4` },
}

const bodyParameters = {
  key: 'value',
}

const fetchCustomerData = (url: string) =>
  axios
    .get<any>(url, config)
    .then(function (response) {
      console.log('bb', response?.data)
      return response.data
    })
    .catch(function (error) {
      console.log(error)
    })

// const fetchTransactionVerification = (url: string) =>
//   axios
//     .post<Response>(url, {
//       money: 123,
//       maritalStatus: 'Flintstone',
//     })
//     .then(function (response) {
//       console.log('aa', response?.data)
//       return response.data
//     })
//     .catch(function (error) {
//       console.log(error)
//     })

const Home: NextPage = () => {
  // const { data, error } = useSWR(
  //   'http://192.168.1.12:5444/api',
  //   fetchTransactionVerification
  // )
  // const { data, error } = useSWR(
  //   'https://developer.banking.asseco.pl/api/cb/party-data-management/v1/customers/persons',
  //   fetchCustomerData
  // )

  const [rows, setRows] = useState<any>([])

  const fetchTransactionVerification = (url: string) =>
    axios
      .get<any>(url)
      .then(function (response) {
        // console.log('aa', response?.data)
        // return response.data
        const { data } = response
        const obj = JSON.parse(data)
        obj.id = rows.length + 1
        obj.correctness = obj.correctness >= 0.1 ? 'yes' : 'no'
        setRows((prevState: any) => [...prevState, obj])
      })
      .catch(function (error) {
        console.log(error)
      })

  // useEffect(() => {
  //   if (!data) {
  //     return
  //   }
  //   const getData = async () =>
  //     await fetchTransactionVerification('http://192.168.1.12:5444/api')
  //   setTransactionResults((prev: any) => {
  //     return [...prev, getData()]
  //   })
  // }, [data])

  // if (error) return <div>failed to load</div>
  // if (!data) return <div>loading...</div>

  const classes = useStyles()
  console.log('transactionResults', rows)
  return (
    <div>
      <CssBaseline />
      <Head>
        <title>Asseco</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      {/* hello {data}! */}
      <Button
        variant="contained"
        onClick={() =>
          fetchTransactionVerification('http://192.168.1.12:5444/api')
        }
        style={{ margin: '5vh', padding: '0.5rem' }}
      >
        Get Transaction
      </Button>
      <div style={{ height: '90vh', width: '100%' }} className={classes.root}>
        <DataGrid
          rows={rows}
          columns={columns}
          // pageSize={5}
          // rowsPerPageOptions={[5]}
          // checkboxSelection
          disableSelectionOnClick
          density="compact"
          getRowClassName={(params) =>
            `super-app-theme--${params.getValue(params.id, 'correctness')}`
          }
        />
      </div>
    </div>
  )
}

export default Home
