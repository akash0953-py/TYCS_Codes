// SPDX-License-Identifier: MIT
pragma solidity >= 0.8.34;

contract Employee {
    struct emp{
        uint8 empid;
        string name;
        uint256 salary;
        string dept;
    }
    mapping (uint8 => emp) public idtoemp;
    emp[] public employees;

    function addemp(uint8 id, string memory nm , uint256 sal , string memory dep) public {
        emp memory a = emp({empid:id , name:nm , salary:sal , dept:dep });
        idtoemp[id] = a;
        employees.push(a);
    }

    function getemp(uint8 id) public view returns (emp memory){
        return idtoemp[id];
    }

    function addbonus(uint8 id) public {
        if (idtoemp[id].salary < 10000){
            idtoemp[id].salary += 5000;
            for (uint8 i=0 ; i<  employees.length ; i++){
                if (employees[i].empid == id){
                    employees[i].salary = idtoemp[i].salary;
                    break;
                }
            }
        }
    }

    function gettotalemp() public view returns (uint){
        return employees.length;
    }
}