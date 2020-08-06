within FMIRaven.Examples;
model BasicTest
  Models.LorenzSystem_Parameters Parameters(
    sigma=sigma.k,
    rho=rho.k,
    beta=beta.k)
    annotation (Placement(transformation(extent={{-10,20},{10,40}})));
  Models.LorenzSystem_Inputs Inputs(
    sigma=sigma.y,
    rho=rho.y,
    beta=beta.y)
    annotation (Placement(transformation(extent={{-10,-8},{10,12}})));
  Models.LorenzSystem_Connectors Connectors
    annotation (Placement(transformation(extent={{-10,-40},{10,-20}})));
  Modelica.Blocks.Sources.Constant sigma(k=10)
    annotation (Placement(transformation(extent={{-80,20},{-60,40}})));
  Modelica.Blocks.Sources.Constant rho(k=28)
    annotation (Placement(transformation(extent={{-80,-10},{-60,10}})));
  Modelica.Blocks.Sources.Constant beta(k=8/3)
    annotation (Placement(transformation(extent={{-80,-40},{-60,-20}})));
equation
  connect(sigma.y, Connectors.sigma) annotation (Line(points={{-59,30},{-20,30},
          {-20,-22},{-12,-22}}, color={0,0,127}));
  connect(rho.y, Connectors.rho) annotation (Line(points={{-59,0},{-30,0},{-30,
          -30},{-12,-30}}, color={0,0,127}));
  connect(beta.y, Connectors.beta) annotation (Line(points={{-59,-30},{-40,-30},
          {-40,-37.2},{-12,-37.2}}, color={0,0,127}));
  annotation (Icon(coordinateSystem(preserveAspectRatio=false)), Diagram(
        coordinateSystem(preserveAspectRatio=false)));
end BasicTest;
