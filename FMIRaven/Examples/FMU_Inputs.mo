within FMIRaven.Examples;
model FMU_Inputs

  FMUs.FMIRaven_Models_LorenzSystem_Inputs_fmu fmu(
    sigma=10,
    rho=28,
    beta=8/3) annotation (Placement(transformation(extent={{-10,-10},{10,10}})));

  // Does not work. Variability is higher that allowed (i.e., constant)
  // fmu(sigma=sigma.y,rho=rho.y,beta=beta.y)
  // fmu(sigma=sigma.k,rho=rho.k,beta=beta.k)

equation

  // Below does not work... FMU assumes "inputs" are constants. See modelDescription.xml
 // fmu.sigma = sigma.y;
 // fmu.rho = rho.y;
 // fmu.beta = beta.y;

  annotation (Icon(coordinateSystem(preserveAspectRatio=false)), Diagram(
        coordinateSystem(preserveAspectRatio=false)));
end FMU_Inputs;
