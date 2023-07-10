/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.lista1;

/**
 *
 * @author joaop
 */
public class Data {
    int dia;
  int mes;
  int ano;

  Data() {
  }

  Data(int ano){
    dia = 1;
    mes = 1;
    this.ano = ano;
  }

  Data(int dia, int mes, int ano){
    this.dia = dia;
    this.mes = mes;
    this.ano = ano;
  }

  String formatarData(String sep){
    return (dia + sep + mes + sep + ano);
  }
}
