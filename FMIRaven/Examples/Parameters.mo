within FMIRaven.Examples;
model Parameters
  Models.LorenzSystem_Parameters fmu(
    sigma=sigma.k,
    rho=rho.k,
    beta=beta.k)
    annotation (Placement(transformation(extent={{-10,-10},{10,10}})));
  Modelica.Blocks.Sources.Constant sigma(k=10)
    annotation (Placement(transformation(extent={{-80,20},{-60,40}})));
  Modelica.Blocks.Sources.Constant rho(k=28)
    annotation (Placement(transformation(extent={{-80,-10},{-60,10}})));
  Modelica.Blocks.Sources.Constant beta(k=8/3)
    annotation (Placement(transformation(extent={{-80,-40},{-60,-20}})));
  annotation (Icon(coordinateSystem(preserveAspectRatio=false)), Diagram(
        coordinateSystem(preserveAspectRatio=false)));
end Parameters;
