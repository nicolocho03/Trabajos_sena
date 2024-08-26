Console.WriteLine("Bienvenido al banco WCG");
Console.WriteLine("Ingrese su nombre: ");
string nombre = Console.ReadLine();

Console.WriteLine("Ingrese su número de documento: ");
float n_identificacion = float.Parse(Console.ReadLine());

Console.WriteLine("Ingrese la cantidad de dinero que desea cambiar");
decimal dinero = decimal.Parse(Console.ReadLine());

decimal dolar = 4035;
decimal euro = 4523;
decimal yen = 27;
decimal peso_mexicano = 211;
decimal libra_esterlina = 5322;

decimal porcentajeIntermediacion = 0;
decimal cambioMoneda = 0;
string monedaOrigen = "Pesos Colombianos";
string monedaDestino = "";
bool salir = false;

while (!salir) 
{
    try 
    {
        Console.WriteLine("Seleccione una divisa para hacer el cambio de moneda.");
        Console.WriteLine("1. Dolar");
        Console.WriteLine("2. Euro");
        Console.WriteLine("3. Yen");
        Console.WriteLine("4. Peso Mexicano");
        Console.WriteLine("5. Libra Esterlina");
        Console.WriteLine("6. Salir");
        int opcion = Convert.ToInt32(Console.ReadLine());

        switch (opcion) 
        {
            case 1:
                monedaDestino = "Dólar";
                porcentajeIntermediacion = 0.02m; 
                cambioMoneda = dinero / dolar;
                break;
            case 2:
                monedaDestino = "Euro";
                porcentajeIntermediacion = 0.03m; 
                cambioMoneda = dinero / euro;
                break;
            case 3:
                monedaDestino = "Yen";
                porcentajeIntermediacion = 0.015m; 
                cambioMoneda = dinero / yen;
                break;
            case 4:
                monedaDestino = "Peso Mexicano";
                porcentajeIntermediacion = 0.01m; 
                cambioMoneda = dinero / peso_mexicano;
                break;
            case 5:
                monedaDestino = "Libra Esterlina";
                porcentajeIntermediacion = 0.05m; 
                cambioMoneda = dinero / libra_esterlina;
                break;
            case 6:
                salir = true; 
                Console.WriteLine("Gracias por usar el programa.");
                continue;
            default:
                Console.WriteLine("Opción no válida, por favor seleccione de nuevo.");
                continue;
        }

     
        decimal montoIntermediacion = dinero * porcentajeIntermediacion;
        decimal totalEnPesos = dinero - montoIntermediacion;
        
        if (montoIntermediacion > dinero * 0.10m) 
        {
            Console.WriteLine($"El porcentaje de intermediación supera el 10% ({montoIntermediacion} pesos). ¿Desea continuar? (s/n)");
            string respuesta = Console.ReadLine();
            if (respuesta.ToLower() != "s") 
            {
                Console.WriteLine("Operación cancelada.");
                continue;
            }
        }

        cambioMoneda = Math.Round(cambioMoneda, 2);
        Console.WriteLine($"Nombre: {nombre}");
        Console.WriteLine($"Documento de Identidad: {n_identificacion}");
        Console.WriteLine($"Moneda Origen: {monedaOrigen}");
        Console.WriteLine($"Moneda Destino: {monedaDestino}");
        Console.WriteLine($"Monto a Cambiar: {dinero} pesos");
        Console.WriteLine($"Monto de Intermediación: {montoIntermediacion} pesos");
        Console.WriteLine($"El cambio de los {dinero} pesos es igual a {cambioMoneda} {monedaDestino}.");

    }
    catch (Exception ex)
    {
        Console.WriteLine("Error: " + ex.Message);
    }
}
