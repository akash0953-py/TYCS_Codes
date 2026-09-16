// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Employee {

    struct Emp {
        uint emp_id;
        string emp_name;
        uint emp_salary;
        string emp_dept;
    }

    Emp[] public employees;

    // Add Employee
    function addEmployee(
        uint _id,
        string memory _name,
        uint _salary,
        string memory _dept
    ) public {

        employees.push(
            Emp({
                emp_id: _id,
                emp_name: _name,
                emp_salary: _salary,
                emp_dept: _dept
            })
        );
    }

    // Display Employee Details
    function getEmployee(uint index)
        public
        view
        returns (
            uint,
            string memory,
            uint,
            string memory
        )
    {
        Emp memory e = employees[index];

        return (
            e.emp_id,
            e.emp_name,
            e.emp_salary,
            e.emp_dept
        );
    }

    // Add Bonus if salary < 10000
    function addBonus(uint index) public {

        if (employees[index].emp_salary < 10000) {
            employees[index].emp_salary += 5000;
        }
    }

    // Total Employees
    function totalEmployees() public view returns(uint){
        return employees.length;
    }
}