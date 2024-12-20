GET_COMPANY_INFO = """
query GetCompanyInfo {
  company {
    founder
    founded
    launch_sites
    headquarters {
      address
      city
      state
    }
    name
    valuation
    vehicles
  }
}
"""