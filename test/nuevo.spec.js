const expect = require("chai").expect;
const newAdm = require("../public/javascripts/verificacion.js")


describe("Probando Modulo verificacion",()=>{
    it("Email y password coinciden", () =>{
        const result = newAdm.comparacion("correo@correo.com", "correo@correo.com","123123", "123123");
        expect(result).to.be.equals(true);
    });
    it("Email distinto y password coinciden", () =>{
        const result = newAdm.comparacion("correo@co.com", "correo@correo.com","123123", "123123");
        expect(result).to.be.equals(false);
    });
    it("Email iguales y password distintos", () =>{
        const result = newAdm.comparacion("correo@correo.com", "correo@correo.com","123123", "123522");
        expect(result).to.be.equals(false);
    });
     it("Email distintos y password distintos", () =>{
        const result = newAdm.comparacion("correo@co.com", "correo@correo.com","123123", "123522");
        expect(result).to.be.equals(false);
    });
})